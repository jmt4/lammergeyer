import datetime

from .base import FunctionalTest
import reminders.timezone_object as tzobj
from reminders.models import List, Reminder
from accounts.models import CustomUser

class LoginRequiredTest(FunctionalTest):

	def setUp(self):
		utc = tzobj.UTC()
		date = datetime.datetime(2015, 06, 23, tzinfo=utc)
		self.list_ = List.objects.create()
		self.reminder = Reminder.objects.create(
			title='Buy milkshakes',
			alarm=date,
			snooze=5,
			repeat=10,
			list=self.list_
		)
		super(LoginRequiredTest, self).setUp()

	def test_reminder_urls_redirect_if_not_logged_in(self):
		# Del tries to reach the reminder app without logging in by going directly
		# to the reminders home url but Del is redirected because he hasn't logged
		# in.

		self.browser.get('%s%s' % (self.server_url, '/reminders/home/',))
		self.assertRegexpMatches(self.browser.current_url, '/accounts/login.+')

		# Del then thinks "Well I already made a reminder, let me type in the url
		# for a reminder list". Del does this but is redirected still to the login
		# page.
		reminder_list_url = '%s%s%s/' % (self.server_url, '/reminders/', self.list_.id,)
		self.browser.get(reminder_list_url)
		self.assertRegexpMatches(self.browser.current_url, '/accounts/login.+')

		# Befuddled, Del tries to edit his reminder but is still redirected
		self.browser.get('%s%s%s%s%s' % 
			(self.server_url, '/reminders/', self.list_.id, '/edit_reminder/', self.reminder.pk,)
		)
		self.assertRegexpMatches(self.browser.current_url, '/accounts/login.+')

		self.login_test_user()

		# Del is taken to the reminders home page
		self.assertRegexpMatches(self.browser.current_url, '/reminders/home/')

		# Then Del visits his only reminder list
		
		self.browser.get(reminder_list_url)
		self.assertRegexpMatches(self.browser.current_url, '/reminders/%s/' % (self.list_.id,))