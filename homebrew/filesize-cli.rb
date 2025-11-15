# Homebrew formula for filesize-cli
# To install:
#   brew install filesize-cli

class FilesizeCli < Formula
  include Language::Python::Virtualenv

  desc "Calculate file and directory sizes from the command line"
  homepage "https://github.com/thaikolja/filesize-cli"
  url "https://github.com/thaikolja/filesize-cli/archive/refs/tags/v2.0.0.tar.gz"
  sha256 "placeholder_for_actual_sha256"
  license "MIT"

  depends_on "python@3.11"

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/filesize", "--version"
    system "#{bin}/filesize", "--help"
  end
end