class ServiceManager:
	def init(self):
		self.services = {}
	def register_service(self, name, service):
		self.services[name] = service
