{
  inputs = {
    nixpkgs = {
      url = "github:nixos/nixpkgs/nixos-unstable";

    };
    flake-utils = {
      url = "github:numtide/flake-utils";
    };
  };
  outputs = { nixpkgs, flake-utils, ... }: flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs {
        inherit system;
      };
      #packageOverrides = pkgs.callPackage ./python-packages.nix {};
      #python3 = pkgs.python3.override { inherit packageOverrides; };
    in {
      devShell = pkgs.mkShell {
        name = "python-venv";
        venvDir = "./.venv";
        buildInputs = with pkgs; [
            R
            rPackages.XML
            rPackages.censusapi
            rPackages.crsuggest
            rPackages.elevatr
            rPackages.geobr
            rPackages.geodata
            rPackages.geofacet
            rPackages.ggbeeswarm
            rPackages.ggiraph
            rPackages.ggridges
            rPackages.GWmodel
            rPackages.gpx
            rPackages.htmlwidgets
            rPackages.httr
            rPackages.inegiR
            rPackages.ipumsr
            rPackages.jsonlite
            rPackages.leaflet
            rPackages.leaflet_extras
            rPackages.leaflet_extras2
            rPackages.lehdr
            rPackages.mapboxapi
            rPackages.mapview
            rPackages.maps
            rPackages.osmdata
            rPackages.pagedown
            rPackages.patchwork
            rPackages.plotly
            rPackages.raster
            rPackages.readr
            rPackages.reticulate
            rPackages.rnaturalearth
            rPackages.rnaturalearthdata
            rPackages.segregation
            rPackages.sf
            rPackages.spatialreg
            rPackages.spdep
            rPackages.srvyr
            rPackages.survey
            rPackages.tidycensus
            rPackages.tidyr
            rPackages.terra
            rPackages.tidygeocoder
            rPackages.tidyterra
            rPackages.tidyverse
            rPackages.tidyUSDA
            rPackages.tigris
            rPackages.tmap
            rPackages.trackeR
            rPackages.trajr
            rPackages.tsibble
            rPackages.viridis
            rPackages.webshot
            rPackages.xml2
            chromium
            pandoc
            texlive.combined.scheme-full
            rstudio
            quarto
          (python3.withPackages(ps: with ps; [
            ipython
            pip
            jupyter
            widgetsnbextension
            googlemaps
            ipympl
            jupyter-nbextensions-configurator
            jedi-language-server
            osmnx
            ipywidgets
            libpysal
            mypy
            hvplot
            pandas
            us
            seaborn
            numpy
            geopandas
            geodatasets
            pyogrio
            geopy
            matplotlib
            pyproj
            osmpythontools
            folium
            mapclassify
            scipy
            networkx
            shapely
            xarray
            rioxarray
            dask
            intake
            intake-parquet
            pooch
            fiona
            plotly
            s3fs
            rasterio
          ]))
        ];
        postVenvCreation = ''
          unset SOURCE_DATE_EPOCH
          pip install -r requirements.txt
        '';

        shellHook = ''
            export BROWSER=brave
                # Tells pip to put packages into $PIP_PREFIX instead of the usual locations.
    # See https://pip.pypa.io/en/stable/user_guide/#environment-variables.
            export PIP_PREFIX=$(pwd)/venvDir
            export PYTHONPATH="$PIP_PREFIX/${pkgs.python3.sitePackages}:$PYTHONPATH"
            export PATH="$PIP_PREFIX/bin:$PATH"
            unset SOURCE_DATE_EPOCH
            #jupyter lab
        '';

        postShellHook = ''
          # allow pip to install wheels
          unset SOURCE_DATE_EPOCH
        '';
      };
    }
  );
}
