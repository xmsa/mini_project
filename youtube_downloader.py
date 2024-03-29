import os
from sys import path
from pytube import YouTube


class YouTube_Downloader:
    def __init__(self, verbose: bool = False) -> None:
        """
        :param verbose: 
            explain what is being done
        :type verbose: bool 
        """
        self.__verbose = verbose

    def download_by_url(self, url) -> None:
        """
        download media with url
        :param url:
            A valid YouTube watch URL.
        :type url: str 
        """
        if url.lower().startswith("https://"):
            self.__download(url)
        else:
            print("Error")
        print("Done ...")

    def download_by_txt_file(self, input_path: str) -> None:
        """
            Download with text file or multiple text files
            To download multiple files, you must enter the path of the files Directory
        :param input_path:
            path dir or text file (format: txt file)
        :type input_path: str
        """
        if os.path.exists(input_path):
            self.__find_txt(input_path)
        else:
            print("Error")
        print("Done ...")

    def __find_txt(self, input_path: str) -> None:
        """
        find Text file
        :param input_path:
            path dir or text file (format: txt file)
        :type input_path: str

        """
        if os.path.isdir(input_path):
            list_txt = os.listdir(input_path)
            for i in list_txt:
                file_path = f"{input_path}/{i}"
                if i.endswith('.txt') and os.path.isfile(file_path):
                    self.__read_txt(file_path, input_path)
        elif os.path.isfile(input_path) and os.path.isfile(input_path):
            file_path = input_path
            input_path = os.path.split(input_path)[0]
            self.__read_txt(file_path, input_path)
        else:
            print('Error: File not found')
            return

    def __read_txt(self, file_path: str, path_dir: str) -> None:
        """
        read Text file
        :param file_path:
            path text file (format: txt file)
        :type file_path: str 
        :param path_dir:
            path directory 
        :type path_dir: str 
        """
        with open(file_path, 'r') as file:
            for url in file.readlines():
                url = url.rstrip()
                if url == "" or not url.lower().startswith("https://"):
                    self.__verbose and print(f'ignore: "{url}"')
                    continue
                self.__verbose and print(f"----------------")
                self.__verbose and print(f"path: {path_dir}")

                self.__download(url, path_dir)
                self.__verbose and print(f"----------------")

    def __download(self, url: str, dir: str = None) -> None:
        """
        Download Media
        :param str url:
            path dir or text file (format: txt file)
        :type url: str
        :param dir_path:
            (optional) Output path for writing media file. If one is not
            specified, defaults to the current working directory.
        :type output_path: str or None
        """
        try:

            yt = YouTube(url)
            self.__verbose and print(f"url: {url}")
            yt.streams.get_highest_resolution().download(output_path=dir)
            self.__verbose and print(f"Download completed")
        except Exception as ex:
            print(f"error({ex}) {url}")


def print_diss():
    print("python youtube_downloader.py [url or file_name.txt] ")


def main():
    if len(sys.argv) == 2:
        yd = YouTube_Downloader(verbose=True)
        if sys.argv[1].endswith(".txt"):
            yd.download_by_txt_file(input_path=sys.argv[1])
        else:
            yd.download_by_url(sys.argv[1])
        return None
    print_diss()


if __name__ == "__main__":
    main()
