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
            rPackages.pagedown
            rPackages.tidyverse
            rPackages.sf
            rPackages.terra
            rPackages.leaflet
            rPackages.leaflet_extras
            rPackages.leaflet_extras2
            rPackages.maps
            rPackages.leafsync
            rPackages.elevatr
            rPackages.patchwork
            rPackages.XML
            rPackages.xml2
            rPackages.gpx
            rPackages.tidygeocoder
            rPackages.crsuggest
            rPackages.rnaturalearth
            rPackages.rnaturalearthdata
            rPackages.osmdata
            rPackages.viridis
            rPackages.tmap
            rPackages.plotly
            rPackages.geodata
            rPackages.tidyterra
            rPackages.htmlwidgets
            rPackages.trackeR
            rPackages.trajr
            rPackages.webshot
            rPackages.reticulate
            chromium
            pandoc
            texlive.combined.scheme-full
            rstudio
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
