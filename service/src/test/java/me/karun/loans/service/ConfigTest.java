package me.karun.loans.service;

import org.junit.Rule;
import org.junit.Test;
import org.junit.contrib.java.lang.system.ClearSystemProperties;

import static org.assertj.core.api.Assertions.assertThat;

public class ConfigTest {

  private static final String fileName = "hitchhikers-guide";
  private static final String key = "answer.to.life.the.universe.and.everything";
  @Rule
  public final ClearSystemProperties clearCustomProperty = new ClearSystemProperties(key);

  @Test
  public void getInt_whenContainsAPropertiesKey_thenReturnsThePropertyValue() {
    final int result = new Config(fileName).getInt(key);

    assertThat(result).isEqualTo(42);
  }

  @Test
  public void getInt_whenContainsASystemValue_thenReturnsTheSystemValue() {
    System.setProperty("actual." + key, "54");

    final int result = new Config(fileName).getInt("actual." + key);

    assertThat(result).isEqualTo(54);
  }

  @Test
  public void getInt_whenContainsASystemValueAndPropertiesKey_thenReturnsTheSystemValue() {
    System.setProperty(key, "54");

    final int result = new Config(fileName).getInt(key);

    assertThat(result).isEqualTo(54);
  }
}
