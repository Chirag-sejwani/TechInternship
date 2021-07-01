"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist

'''
class Playlist:
    def __init__ (self, playlist_Name):
        self.Playlist_Name = playlist_Name
        self.Playlist_Videos = []
    def GetName(self):
        return self.Playlist_Name
    def AddVideo(self, Name):
        self.Playlist_Videos = Name
    def GetVideos(self,Name):
        return self.Playlist_Videos
'''



List = []


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_Playing = None
        self._video_paused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        temp_list = []

        for vid in videos:

            # Convoluted way to display tags in required format
            tags ="["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags)-2] + "]"

            # Put all videos in a list for sorting
            temp_list += [f"{vid.title} ({vid.video_id}) {tags}"]

        # Sort the list and display
        sorted_list = sorted(temp_list)
        for x in sorted_list:
            print(x)

    def play_video(self, video_id):
        if self._video_Playing == None:
            videos = self._video_library.get_all_videos()
            vide = 'not found'
            for vid in videos:
                if vid.video_id == video_id:
                    vide = vid.title
            if vide == 'not found':
                print('Cannot play video: Video does not exist')
            else:
                print('Playing video:', vide)
            self._video_Playing = vide
            self._video_paused = False
        else:
            videos = self._video_library.get_all_videos()
            vide = 'not found'
            for vid in videos:
                if vid.video_id == video_id:
                    vide = vid.title
            if vide == 'not found':
                print('Cannot play video: Video does not exist')
            else:
                print('Stopping video:', self._video_Playing)
                self._video_Playing = None
                print('Playing video:', vide)
                self._video_Playing = vide
            self._video_paused = False


# this searches the video ID from the list of books and then gets its book title from the pointer

    def stop_video(self):
        if self._video_Playing == None:
            print("Cannot stop video: No video is currently playing")
        else:
            print('Stopping video:', self._video_Playing)
            self._video_Playing = None

    def play_random_video(self):
        import random
        videos = self._video_library.get_all_videos()
        self.play_video(videos[random.randint(0, (len(videos)-1))].video_id)

    def pause_video(self):
        if self._video_Playing == None:
            print('Cannot pause video: No video is currently playing')
            return
        if self._video_paused == False:
            print('Pausing video:', self._video_Playing)
            self._video_paused = True
        else:
            print('Video already paused:', self._video_Playing)

    def continue_video(self):
        if self._video_Playing == None:
            print("Cannot continue video: No video is currently playing")
            return
        if self._video_paused == True:
            print('Continuing video:', self._video_Playing)
            self._video_paused = False
        else:
            print('Cannot continue video: Video is not paused')

    def show_playing(self):
        if self._video_Playing != None and self._video_paused == False:
            videos = self._video_library.get_all_videos()
            a = str
            for vid in videos:
                if vid.title == self._video_Playing:
                    i ="["
                    for tag in vid.tags:
                        i = i + tag + " "
                    i = i + "]"

                    if i != "[]":
                        i = i[0:len(i)-2] + "]"
                    print('Currently playing: '+ vid.title + ' (' + vid.video_id + ') ' + i)
        elif self._video_Playing != None and self._video_paused == True:
            videos = self._video_library.get_all_videos()
            a = str
            for vid in videos:
                if vid.title == self._video_Playing:
                    i ="["
                    for tag in vid.tags:
                        i = i + tag + " "
                    i = i + "]"

                    if i != "[]":
                        i = i[0:len(i)-2] + "]"
                    print('Currently playing: '+ vid.title + ' (' + vid.video_id + ') ' + i + ' - PAUSED')
        else:
            print('No video is currently playing')


    def create_playlist(self, playlist_name):
        global List
        a = int
        if len(List) == 0 :
            a = 0
            Mylist = Playlist(playlist_name)
            List.append(Mylist)
            print('Successfully created new playlist:', List[a].GetName())
            return
        Found = False
        for i in range (0,(len(List))):
            if List[i].GetName().lower() == playlist_name.lower():
                Found = True
        if Found == True:
            print('Cannot create playlist: A playlist with the same name already exists')
        else:
            a = len(List)
            Mylist = Playlist(playlist_name)
            List.append(Mylist)
            print('Successfully created new playlist:', List[a].GetName())
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

    def add_to_playlist(self, playlist_name, video_id):
        videos = self._video_library.get_all_videos()
        vide = 'not found'
        for vid in videos:
            if vid.video_id == video_id:
                vide = vid.title
        if vide == 'not found':
            print('Cannot add video to my_cool_playlist: Video does not exist')
            return
        Found = False
        for i in range (0,(len(List))):
            if List[i].GetName().lower() == playlist_name.lower():
                a = i
                Found = True
        if Found == True:
            List[a].AddVideo(vide)
            print('Added video to ' + playlist_name + ': ' + vide)
        else:
            print('Cannot add video to another_playlist: Playlist does not exist')

        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

    def show_all_playlists(self):
        temp_list=[]
        if len(List) == 0:
            print('No playlists exist yet')
            return
        for i in range (0,(len(List))):
            temp_list.append(List[i].GetName())
        sorted_list = sorted(temp_list)
        print('Showing all playlists:')
        for x in sorted_list:
            print(x)
            



        """Display all playlists."""

    

    def show_playlist(self, playlist_name):
        a=int
        for i in range(0,(len(List))):
            if List[i].GetName().lower() == playlist_name.lower():
                a = i
                Found = True
        if Found == True:
            if len(List[a].GetVideos) == 0:
                print('No videos here yet')
                return
            print('Showing playlist:', List[a].GetName)
            for i in range(0,len(List[a].GetVideos)):
                videos = self._video_library.get_all_videos()
                a = str
                for vid in videos:
                    if vid.title == List[a].GetVideos[i]:
                        i ="["
                    for tag in vid.tags:
                        i = i + tag + " "
                    i = i + "]"

                    if i != "[]":
                        i = i[0:len(i)-2] + "]"
                    print(vid.title + ' (' + vid.video_id + ') ' + i)



    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
