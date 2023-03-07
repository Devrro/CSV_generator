COMPANIES_NAME = ["AT&T", "MeadWestvaco", "Humana", "Murphy Oil", "Medco Health Solutions",
                  "Western & Southern Financial Group", "General Electric", "Hershey", "Lear", "Molina Healthcare",
                  "Limited Brands", "Henry Schein", "URS", "eBay", "FirstEnergy", "Publix Super Markets",
                  "United Parcel Service", "Cardinal Health", "American Family Insurance Group", "Halliburton",
                  "Owens Corning", "Alpha Natural Resources", "Danaher", "Ball", "Bristol-Myers Squibb",
                  "Interpublic Group", "Wells Fargo", "Procter & Gamble", "Coca-Cola Enterprises", "Commercial Metals",
                  "Sears Holdings", "HCA Holdings", "Omnicom Group", "Mylan", "BlackRock", "American Electric Power",
                  "CarMax", "Celgene", "Dick's Sporting Goods", "Graybar Electric", "Marsh & McLennan", "Aflac",
                  "DuPont", "NII Holdings", "BorgWarner", "Micron Technology", "Auto-Owners Insurance", "Jarden",
                  "Harris", "Motorola Solutions", "Guardian Life Ins. Co. of America", "MGM Resorts International",
                  "EMC", "Eaton", "Genworth Financial", "Apache", "Starwood Hotels & Resorts",
                  "MetroPCS Communications", "Caesars Entertainment", "Travelers Cos.", "AMR", "SanDisk",
                  "CC Media Holdings", "BrightPoint", "FMC Technologies", "United Stationers", "General Cable", "Aon",
                  "McDonald's", "Enbridge Energy Partners", "PG&E Corp.", "Fannie Mae", "INTL FCStone", "Stryker",
                  "Reliance Steel & Aluminum", "ConocoPhillips", "Catalyst Health Solutions", "Group 1 Automotive",
                  "Sempra Energy", "Freddie Mac", "Rockwell Automation", "Qualcomm", "Western Union",
                  "Jacobs Engineering Group", "Mutual of Omaha Insurance", "Whole Foods Market",
                  "Massachusetts Mutual Life Insurance", "Southern", "Express Scripts Holding", "Emcor Group",
                  "Dana Holding", "Reinsurance Group of America", "Owens-Illinois", "Hess", "CMS Energy",
                  "Pitney Bowes", "Avon Products", "Costco Wholesale", "Applied Materials", "Computer Sciences", "Gap",
                  "Ingram Micro", "Tyson Foods", "HollyFrontier", "Hertz Global Holdings", "L-3 Communications",
                  "Cliffs Natural Resources", "Cameron International", "Penske Automotive Group", "Kroger",
                  "Dollar General", "Huntsman", "Estée Lauder", "Sprint Nextel", "MasterCard", "NextEra Energy",
                  "Sonic Automotive", "AECOM Technology", "Reynolds American", "Thermo Fisher Scientific",
                  "Exxon Mobil", "Tenneco", "Macy's", "Land O'Lakes", "Spectrum Group International",
                  "Advanced Micro Devices", "Viacom", "Dell", "World Fuel Services", "YRC Worldwide",
                  "Newell Rubbermaid", "WellPoint", "Alcoa", "McGraw-Hill", "MetLife", "Corning", "Assurant",
                  "Steel Dynamics", "Union Pacific", "Toys "R" Us", "Visa", "Timken", "Comcast", "Johnson Controls",
                  "DirecTV", "CVS Caremark", "Praxair", "Kohl's", "AES", "Deere", "Allstate", "El Paso",
                  "Air Products & Chemicals", "Staples", "State Farm Insurance Cos.", "Peter Kiewit Sons'",
                  "Eastman Kodak", "CSX", "General Mills", "United Services Automobile Assn.", "Coca-Cola", "Celanese",
                  "Cigna", "State Street Corp.", "Pacific Life", "Weyerhaeuser", "Big Lots", "Energy Transfer Equity",
                  "Telephone & Data Systems", "Northwestern Mutual", "C.H. Robinson Worldwide", "Tech Data",
                  "H.J. Heinz", "SunGard Data Systems", "Kindred Healthcare", "Autoliv", "Baker Hughes",
                  "J.P. Morgan Chase & Co.", "Kellogg", "NiSource", "Exelon", "Susser Holdings", "Nash-Finch",
                  "Global Partners", "Frontier Communications", "Spectra Energy", "Pepco Holdings",
                  "Advance Auto Parts", "OfficeMax", "Wal-Mart Stores", "Intel", "Constellation Energy", "Starbucks",
                  "AutoNation", "Sysco", "United States Steel", "Archer Daniels Midland",
                  "Thrivent Financial for Lutherans", "Laboratory Corp. of America", "Xerox", "J.M. Smucker",
                  "AmerisourceBergen", "Nationwide", "Textron", "Marathon Oil", "Becton Dickinson", "KeyCorp",
                  "Discover Financial Services", "PepsiCo", "Safeway", "Marriott International", "Rite Aid",
                  "TRW Automotive Holdings", "International Business Machines", "CH2M Hill", "Visteon",
                  "Allegheny Technologies", "Wesco International", "Time Warner Cable", "Raytheon", "Las Vegas Sands",
                  "Sara Lee", "Yahoo", "Exelis", "TravelCenters of America", "Casey's General Stores", "Domtar",
                  "Boston Scientific", "Expeditors International of Washington", "Family Dollar Stores", "Sanmina-SCI",
                  "Host Hotels & Resorts", "Navistar International", "Darden Restaurants", "Consol Energy",
                  "Ameriprise Financial", "Rock-Tenn", "Bemis", "Gilead Sciences", "Ross Stores", "Aetna",
                  "Delta Air Lines", "Chubb", "AGCO", "Anixter International", "Sealed Air", "Core-Mark Holding",
                  "Yum Brands", "Hormel Foods", "SLM", "Automatic Data Processing", "Verizon Communications", "Terex",
                  "J.C. Penney", "Dean Foods", "Aleris", "Lowe's", "Liberty Interactive", "Icahn Enterprises",
                  "Wynn Resorts", "Dow Chemical", "Capital One Financial", "Illinois Tool Works", "International Paper",
                  "Clorox", "U.S. Bancorp", "Pantry", "Apple", "Caterpillar", "Monsanto", "Norfolk Southern", "Merck",
                  "R.R. Donnelley & Sons", "Pfizer", "Aramark", "Charles Schwab", "UGI", "Con-way",
                  "Insight Enterprises", "Consolidated Edison", "CVR Energy", "Cisco Systems",
                  "Live Nation Entertainment", "Nordstrom", "Walgreen", "Amerigroup", "Tenet Healthcare", "Xcel Energy",
                  "AutoZone", "NRG Energy", "Manpower", "Franklin Resources", "Owens & Minor", "SunTrust Banks",
                  "Cognizant Technology Solutions", "Dillard's", "Barnes & Noble", "CIT Group", "3M", "Altria Group",
                  "PPG Industries", "Goodrich", "Public Service Enterprise Group", "W.W. Grainger", "Eastman Chemical",
                  "Great Atlantic & Pacific Tea", "Dole Food", "Avaya", "Nike", "News Corp.", "General Motors",
                  "St. Jude Medical", "Home Depot", "Biogen Idec", "Cablevision Systems", "Universal Health Services",
                  "Alliant Techsystems", "NetApp", "PVH", "Southwest Airlines", "Johnson & Johnson",
                  "Plains All American Pipeline", "Republic Services", "American Express", "Target", "Progressive",
                  "Precision Castparts", "Bank of New York Mellon Corp.", "Amgen", "Western Refining", "Oneok",
                  "Prudential Financial", "Fluor", "Best Buy", "Booz Allen Hamilton Holding", "Hewlett-Packard",
                  "Edison International", "Meritor", "Ally Financial", "Mosaic", "New York Life Insurance", "TJX",
                  "Ashland", "BB&T Corp.", "Calpine", "Rockwell Collins", "Dominion Resources",
                  "Community Health Systems", "Harley-Davidson", "Synnex", "United Continental Holdings",
                  "Texas Instruments", "Dr Pepper Snapple Group", "Baxter International", "Paccar", "Supervalu",
                  "Targa Resources", "Google", "Bed Bath & Beyond", "Bank of America Corp.", "Charter Communications",
                  "Marathon Petroleum", "Freeport-McMoRan Copper & Gold", "Kimberly-Clark", "Lincoln National",
                  "Ralph Lauren", "Health Management Associates", "Oshkosh", "Ryder System", "Arrow Electronics",
                  "Campbell Soup", "Emerson Electric", "Occidental Petroleum", "Liberty Mutual Insurance Group",
                  "Whirlpool", "National Oilwell Varco", "Chevron", "Sherwin-Williams", "Agilent Technologies",
                  "Coventry Health Care", "Newmont Mining", "Avery Dennison", "Goldman Sachs Group", "Omnicare",
                  "PNC Financial Services Group", "Regions Financial", "Eli Lilly", "CenterPoint Energy",
                  "Corn Products International", "CF Industries Holdings", "Abbott Laboratories", "Kinder Morgan",
                  "Principal Financial", "Chesapeake Energy", "Philip Morris International", "Morgan Stanley",
                  "Fidelity National Information Services", "CDW", "Jabil Circuit", "McKesson", "Unum Group",
                  "Waste Management", "Broadcom", "US Airways Group", "W.R. Berkley", "Duke Energy", "Williams",
                  "Centene", "TIAA-CREF", "Amazon.com", "EOG Resources", "Crown Holdings", "Colgate-Palmolive",
                  "Stanley Black & Decker", "Ecolab", "Medtronic", "Oracle", "General Dynamics", "Tesoro",
                  "Office Depot", "O'Reilly Automotive", "Citigroup", "Honeywell International", "KBR",
                  "Progress Energy", "Winn-Dixie Stores", "Erie Insurance Group", "Quest Diagnostics",
                  "Motorola Mobility Holdings", "PPL", "Mohawk Industries", "Ford Motor", "AK Steel Holding",
                  "Energy Future Holdings", "ConAgra Foods", "FedEx", "CenturyLink", "DTE Energy", "SAIC", "Masco",
                  "Avnet", "Kraft Foods", "First Data", "Parker Hannifin", "United Technologies", "NuStar Energy",
                  "Foot Locker", "Goodyear Tire & Rubber", "Allergan", "Western Digital", "CBS", "Gannett", "Symantec",
                  "Enterprise Products Partners", "Shaw Group", "Loews", "Sunoco", "Cummins", "CBRE Group",
                  "Momentive Specialty Chemicals", "Peabody Energy", "Kelly Services", "DISH Network", "Mattel",
                  "Avis Budget Group", "PetSmart", "Devon Energy", "GameStop", "Genuine Parts", "Smithfield Foods",
                  "NCR", "Vanguard Health Systems", "Boeing", "Health Net", "Liberty Global", "Walt Disney",
                  "Lockheed Martin", "Entergy", "Dollar Tree", "SPX", "CHS", "UnitedHealth Group", "Seaboard",
                  "Hartford Financial Services Group", "Microsoft", "Ameren", "WellCare Health Plans", "DaVita",
                  "Fifth Third Bancorp", "Valero Energy", "Time Warner", "Northrop Grumman", "Nucor",
                  "Fidelity National Financial", "Anadarko Petroleum", "Berkshire Hathaway", "MRC Global",
                  "American International Group", "VF", "Dover", ]
