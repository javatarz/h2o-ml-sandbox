from bokeh.plotting import figure, output_file, save, show
from .accuracy_curves import calculate_gini


def make_roc_plot(fallout, recall):
    gini = calculate_gini(fallout, recall)
    plot = figure(title='ROC plot: gini=%s' % gini,
                  x_axis_label="Fallout",
                  y_axis_label="Recall")

    plot.line([0, 1], [0, 1], line_dash="dashed",
              line_color="gray", line_alpha=0.4)
    plot.line(fallout, recall, line_width=2)
    output_file("roc_plot.html", mode="inline")
    save(plot)
    # show(plot)
