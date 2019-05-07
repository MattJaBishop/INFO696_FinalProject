library(ggplot2)

#Create graph in ggplot2

static_plot <- ggplot(data = Table02_NationalHealthExpendituresByType_BillionDollars_NormalizedLevel2) +
  aes(x = Year, y = Cost, color = Type) +
  geom_line() +
  labs(title = "National Health Expenditures",
    x = "Year",
    y = "Cost in Billions") +
  theme_minimal()

#Convert to plotly graph

interactive_plot <- plotly::ggplotly(static_plot)
interactive_plot

#Save to plotly

library(plotly)

api_create(interactive_plot, filename = "FirstGraph")