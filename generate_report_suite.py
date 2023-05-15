from pyunitreport import HTMLTestRunner

# Prueba para sobreescribir la clase HTMLTestRunner de pyunitreport y así
# conseguir que los resultados se impriman completos en un solo archivo
# y no solo se registren los resultados de la ultima prueba como hace HTMLTestRunner
class CustomHTMLTestRunner(HTMLTestRunner):
    def generate_reports(self, result):
        self.generate_report(result)

        combined_report = ""
        for report in self.reports:
            with open(report, 'r') as f:
                combined_report += f.read()

        combined_report_path = self.output + "combined_report.html"
        with open(combined_report_path, 'w') as f:
            f.write(combined_report)
