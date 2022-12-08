from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
class RedirectLoggedInUser:
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('dashboard')
		return super().dispatch(request, *args, **kwargs)

class StaffRequiredMixin:
	def dispatch(self, request, *args, **kwargs):
		if not request.user.is_staff:
			raise PermissionDenied('You are not allowed here!')
		return self.dispatch(request, *args, **kwargs)