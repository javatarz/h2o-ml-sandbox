package me.karun.loans.service;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import hex.genmodel.easy.EasyPredictModelWrapper;
import hex.genmodel.easy.RowData;
import me.karun.loans.service.model.BadLoanModel;

import java.util.Map;

import static java.net.HttpURLConnection.HTTP_OK;
import static me.karun.loans.service.responses.BadLoanResponse.response;
import static spark.Spark.port;
import static spark.Spark.post;

public class App {
  private static final Gson gson = new GsonBuilder().create();
  private static final EasyPredictModelWrapper model = new EasyPredictModelWrapper(new BadLoanModel());
  private static final Config config = new Config("config");

  public static void main(String[] args) {
    port(config.getInt("server.port"));

    post("/score", (req, res) -> {
      res.status(HTTP_OK);
      return gson.toJson(response(model.predictBinomial(with(req.body()))));
    });
  }

  @SuppressWarnings("unchecked")
  private static RowData with(final String requestMessage) {
    final RowData rowData = new RowData();
    rowData.putAll(gson.fromJson(requestMessage, Map.class));
    return rowData;
  }
}

