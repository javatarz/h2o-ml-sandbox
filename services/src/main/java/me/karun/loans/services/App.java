package me.karun.loans.services;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonSyntaxException;
import hex.genmodel.easy.EasyPredictModelWrapper;
import hex.genmodel.easy.RowData;
import me.karun.loans.services.model.BadLoanModel;

import java.util.Map;

import static java.net.HttpURLConnection.HTTP_BAD_REQUEST;
import static java.net.HttpURLConnection.HTTP_OK;
import static me.karun.loans.services.responses.BadLoanResponse.response;
import static spark.Spark.*;

public class App {
  private static final Gson gson = new GsonBuilder().create();
  private static final EasyPredictModelWrapper model = new EasyPredictModelWrapper(new BadLoanModel());
  private static final Config config = new Config("config");

  public static void main(String[] args) {
    port(config.getInt("server.port"));
    enableCORS();

    before((req, res) -> res.type("application/json"));
    exception(JsonSyntaxException.class, (exception, request, response) -> {
      response.status(HTTP_BAD_REQUEST);
      response.body("{\"state\":\"\"}");
    });

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

  private static void enableCORS() {
    options("/*", (request, response) -> {

      String accessControlRequestHeaders = request.headers("Access-Control-Request-Headers");
      if (accessControlRequestHeaders != null) {
        response.header("Access-Control-Allow-Headers", accessControlRequestHeaders);
      }

      String accessControlRequestMethod = request.headers("Access-Control-Request-Method");
      if (accessControlRequestMethod != null) {
        response.header("Access-Control-Allow-Methods", accessControlRequestMethod);
      }

      return "OK";
    });

    before((request, response) -> {
      response.header("Access-Control-Allow-Origin", "*");

//      response.header("Access-Control-Allow-Origin", origin);
//      response.header("Access-Control-Request-Method", methods);
//      response.header("Access-Control-Allow-Headers", headers);
    });
  }
}

