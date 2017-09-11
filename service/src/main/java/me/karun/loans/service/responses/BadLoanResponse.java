package me.karun.loans.service.responses;

import hex.genmodel.easy.prediction.BinomialModelPrediction;

public class BadLoanResponse {
  private final boolean badLoan;
  private final double probability;

  private BadLoanResponse(final BinomialModelPrediction result) {
    this.badLoan = "1".equals(result.label);
    this.probability = result.classProbabilities[1];
  }

  public static BadLoanResponse response(final BinomialModelPrediction result) {
    return new BadLoanResponse(result);
  }
}
