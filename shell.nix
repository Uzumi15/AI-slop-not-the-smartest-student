{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python313
    python313Packages.pyside6
  ];

  shellHook = ''
    echo "Окружение NixOS для PySide6 успешно загружено!"
  '';
}