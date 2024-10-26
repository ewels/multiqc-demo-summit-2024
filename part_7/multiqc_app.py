import json

import multiqc
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components
from multiqc.plots import bargraph

# Sidebar
with st.sidebar:
    st.title("MultiQC Streamlit App")
    st.write("Edit below to see the output update in real-time.")

    # Set DATA_PATH in an input
    DATA_PATH = st.text_input("Demo Data URL", "./fastp")


# Set the title
st.title("MultiQC Streamlit App")


# Parse logs
@st.cache_resource()
def parse_data():
    multiqc.parse_logs(DATA_PATH)

    # Print details about what was parsed
    with st.expander("Parsed data details"):
        st.subheader("Modules")
        st.write(multiqc.list_modules())
        st.subheader("Plots")
        st.write(multiqc.list_plots())
        st.subheader("Samples")
        st.write(multiqc.list_samples())


# Show a plot
@st.cache_resource()
def create_plot():
    st.header("fastp plot")
    st.write("This is MultiQC plot from the parsed data.")
    fastp_plot = multiqc.get_plot("fastp", "Insert Sizes")
    fastp_plot_pt = fastp_plot.get_figure(0)
    fastp_plot_pt.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=go.layout.XAxis(),
        yaxis=go.layout.YAxis(),
        modebar=go.layout.Modebar(),
    )
    st.plotly_chart(fastp_plot_pt)


# Add a plot with some custom data
@st.cache_resource()
def custom_plot(data):
    module = multiqc.BaseMultiqcModule(
        anchor="my_metrics",
    )
    custom_plot = bargraph.plot(
        data=json.loads(data),
        pconfig={"id": "my_metrics_barplot", "title": "My metrics"},
    )

    # Show a single plot
    custom_plot_pt = custom_plot.get_figure(0)
    custom_plot_pt.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=go.layout.XAxis(),
        yaxis=go.layout.YAxis(),
        modebar=go.layout.Modebar(),
    )
    st.plotly_chart(custom_plot_pt)

    # Add to report
    module.add_section(plot=custom_plot)
    multiqc.report.modules.append(module)


@st.cache_resource()
def create_report():
    multiqc.write_report(force=True, output_dir="multiqc_report")
    html_data = open("multiqc_report/multiqc_report.html").read()
    components.html(html_data, scrolling=True, height=500)


# Run cached functions
parse_data()
create_plot()

# Custom data + plot
st.header("Custom plot")
st.write("This is a custom plot with some custom data contained in this script.")
EXAMPLE_CUSTOM_DATA = st.text_area(
    "Custom Data",
    """{
    "sample 1": {"aligned": 23542, "not_aligned": 343},
    "sample 2": {"aligned": 1275, "not_aligned": 7328}
}""",
)
custom_plot(EXAMPLE_CUSTOM_DATA)

# Generate the report
st.header("MultiQC Report")
if st.button("Generate", type="primary"):
    create_report()
