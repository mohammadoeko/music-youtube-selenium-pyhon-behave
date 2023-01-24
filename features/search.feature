Feature: Search Feature

Scenario: Input search data and click enter
     Given open web music youtube
     When Click search menu
     And Type sugeng dalu
     And click enter
     Then Display result data sugeng dalu

Scenario: Input does not match search data and click enter
     Given open web music youtube
     When Click search menu
     And Type kulpsihfkshp
     And click enter
     Then Display no result found in the web

Scenario: Input empty search data 
     Given open web music youtube
     When Click search menu
     And Type empty in search
     And click enter
     Then Stay in search menu