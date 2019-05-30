# SPDX-License-Identifier: LGPL-3.0-only

let
  _pkgs = import <nixpkgs> {};
in
{ pkgs ? import (_pkgs.fetchFromGitHub { owner = "NixOS";
                                         repo = "nixpkgs-channels";
                                         # nixos-unstable @2019-05-28
                                         rev = "eccb90a2d997d65dc514253b441e515d8e0241c3";
                                         sha256 = "0ffa84mp1fgmnqx2vn43q9pypm3ip9y67dkhigsj598d8k1chzzw";
                                       }) {}
}:

with pkgs;

mkShell {
  buildInputs = [
    python3
    python3Packages.black
    python3Packages.flake8
    python3Packages.pylama
    python3Packages.pytest
    python3Packages.pytestcov
    python3Packages.requests
    python3Packages.requests-mock
    python3Packages.tox
    python3Packages.twine
    python3Packages.wheel
  ];
}
