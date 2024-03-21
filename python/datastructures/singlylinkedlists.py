# music playlist manager :
'''
each node represents a song : data(store info about the song) next pointer links to the next node 

'''
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Song:
    def __init__(self,title,artist,duration) -> None:
        self.title = title
        self.artist = artist
        self.duration = duration

class Playlist:
    def __init__(self) -> None:
        self.head = None

    # method to add songs playlist 
    def add_song(self,song):
        new_node = Node(song)
        # check if the list has a head node 
        if not self.head:
            self.head = new_node
            return
        # tag the current node 
        current_node = self.head
        # loop to add subsequent nodes 
        # indicating the node pointers 
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # display the playlist 
    def display_playlist(self):
        current_node = self.head
        while current_node:
            print(f"{current_node.data.title} - {current_node.data.artist} - {current_node.data.duration}")
            current_node = current_node.next

    def get_all_songs(self):
        all_songs = []
        current_node = self.head
        while current_node:
            all_songs.append(current_node.data)
            current_node = current_node.next
        print(all_songs[0].title)
        return all_songs


# Test 
playlist = Playlist()
song1 = Song("Shape of You", "Ed Sheeran", 4)
song2 = Song("Shusha Nyavu", "Christina Shusho", 3.5)
song3 = Song("Black Sheep","Joseph Mbugua", 5)
playlist.add_song(song1)
playlist.add_song(song2)
playlist.add_song(song3)

print("Current Playlist")
playlist.display_playlist()

all_songs = playlist.get_all_songs()
print("All songs in playlist")
for song in all_songs:
    print(f"{song.title} - {song.artist} - {song.duration} mins")