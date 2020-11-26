from datetime import datetime


class Task:
	"""Model of a task saved in database."""
	def __init__(
	    self, summary: str, description: str, _datetime: datetime,
	    notification: int
	):
		#TODO ORM
		self.summary = summary
		self.description = description
		self.datetime = _datetime
		self.notification = notification

	def __str__(self):
		string = f"{self.summary} scheduled at {self.datetime}"
		if self.notification is not 0:
			return f"{string}, with notification at {self.notification}"
		return string

	def __repr__(self):
		return f"Task({self.summary}, {self.description}, {self.datetime}, {self.notification})"
