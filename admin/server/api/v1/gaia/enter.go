package gaia

import "github.com/flipped-aurora/gin-vue-admin/server/service"

type ApiGroup struct {
	DashboardApi
	QuotaApi
	ProvidersApi
	TenantsApi
	SystemApi
	TestApi
}

var (
	dashboardService        = service.ServiceGroupApp.GaiaServiceGroup.DashboardService
	tenantsService          = service.ServiceGroupApp.GaiaServiceGroup.TenantsService
	providersService        = service.ServiceGroupApp.GaiaServiceGroup.ProvidersService
	systemIntegratedService = service.ServiceGroupApp.GaiaServiceGroup.SystemIntegratedService
)
var QuotaService = service.ServiceGroupApp.GaiaServiceGroup.QuotaService
var TestService = service.ServiceGroupApp.GaiaServiceGroup.TestService
