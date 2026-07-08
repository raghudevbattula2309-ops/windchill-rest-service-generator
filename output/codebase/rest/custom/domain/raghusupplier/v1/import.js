/*
  TURBOMECA
  Projet GEODE
*/

function function_getraghusupplier(data, params) {

    var helper = Java.type("ext.geode.raghusupplier.spsquery.raghusupplierODataHelper");

    return helper.getraghusupplier(data, params);
}