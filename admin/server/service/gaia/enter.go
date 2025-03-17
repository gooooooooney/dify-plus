package gaia

type ServiceGroup struct {
	SystemIntegratedService
	DashboardService
	QuotaService
	ProvidersService
	TenantsService
	TestService
}
