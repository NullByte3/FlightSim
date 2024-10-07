CREATE TABLE IF NOT EXISTS `airport` (
    `id` int(11) NOT NULL,
    `ident` varchar(40) NOT NULL,
    `type` varchar(40) DEFAULT NULL,
    `name` varchar(40) DEFAULT NULL,
    `latitude_deg` double DEFAULT NULL,
    `longitude_deg` double DEFAULT NULL,
    `elevation_ft` int(11) DEFAULT NULL,
    `continent` varchar(40) DEFAULT NULL,
    `iso_country` varchar(40) DEFAULT NULL,
    `iso_region` varchar(40) DEFAULT NULL,
    `municipality` varchar(40) DEFAULT NULL,
    `scheduled_service` varchar(40) DEFAULT NULL,
    `gps_code` varchar(40) DEFAULT NULL,
    `iata_code` varchar(40) DEFAULT NULL,
    `local_code` varchar(40) DEFAULT NULL,
    `home_link` varchar(40) DEFAULT NULL,
    `wikipedia_link` varchar(40) DEFAULT NULL,
    `keywords` varchar(40) DEFAULT NULL,
    PRIMARY KEY (`ident`)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `country` (
    `iso_country` varchar(40) NOT NULL,
    `name` varchar(40) DEFAULT NULL,
    `continent` varchar(40) DEFAULT NULL,
    `wikipedia_link` varchar(40) DEFAULT NULL,
    `keywords` varchar(40) DEFAULT NULL,
    PRIMARY KEY (`iso_country`)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(40) NOT NULL,
    `score` int(11) DEFAULT 0,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1;