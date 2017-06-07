#coding:utf-8
import twitter
import os

def getAuth():
    consumer_key = ""
    consumer_secret = ""
    token = ""
    token_secret = ""
    auth = twitter.OAuth(consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        token=token,
                        token_secret=token_secret)
    return auth

def main():
    is_upload_img = True
    auth = getAuth()
    t = twitter.Twitter(auth=auth)
    # 投稿するツイート
    status = "あ"
    if is_upload_img:
        # 画像付きツイート
        filename = "test.JPG"
        base_path = os.path.dirname(os.path.abspath(__file__))
        # pic:画像のパス
        pic = os.path.normpath(os.path.join(base_path, './pic/' + filename))
        with open(pic, "rb") as image_file:
            image_data = image_file.read()
        pic_upload = twitter.Twitter(domain='upload.twitter.com', auth=auth)
        id_img1 = pic_upload.media.upload(media=image_data)["media_id_string"]
        try:
            t.statuses.update(status=status, media_ids=",".join([id_img1]))
        except twitter.TwitterHTTPError as e:
            print(e)
    else:
        # ツイートのみ
        try:
            t.statuses.update(status=status)
        except twitter.TwitterHTTPError as e:
            print(e)

if __name__ == '__main__':
    main()
