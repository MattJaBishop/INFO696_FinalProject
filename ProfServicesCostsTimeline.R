library(ggplot2)
library(plyr)

#Create graph in ggplot2

data = TotalHealthExpendituresByType_BillionDollars_NormalizedProfessionalServices

data$prop = ddply(data, "Year", transform, 
                  Percent = Cost / sum(Cost) * 100)

static_plot <- ggplot(data$prop, aes(x = Year, y = Percent, fill = Type)) +
  geom_area(alpha=0.4 , size=.2, colour="black") +
  theme_minimal()

#Convert to plotly graph

interactive_plot <- plotly::ggplotly(static_plot)
interactive_plot

#Save to plotly

library(plotly)

api_create(interactive_plot, filename = "ProfServicesTimeline")