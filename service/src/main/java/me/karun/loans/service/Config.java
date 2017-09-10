package me.karun.loans.service;

import java.util.Optional;
import java.util.ResourceBundle;

public class Config {
  private final ResourceBundle bundle;

  public Config(final String resourceName) {
    this.bundle = ResourceBundle.getBundle(resourceName);
  }

  int getInt(final String key) {
    return Integer.parseInt(get(key).get());
  }

  private Optional<String> get(final String key) {
    final Optional<String> systemProperty = Optional.ofNullable(System.getProperty(key));

    if (systemProperty.isPresent()) {
      return systemProperty;
    }

    if (bundle.containsKey(key)) {
      return Optional.of(bundle.getString(key));
    }

    return Optional.empty();
  }
}
