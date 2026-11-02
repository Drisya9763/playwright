#Radiobutton

#Allows user to choose only one option from a group

from playwright.sync_api import expect 

def test_radio_buttons(page):
    #Step 1: Open radio button URL
    page.goto("https://practice.expandtesting.com/radio-buttons")
    #Step 2: Locate Radio buttons using their labels
    blue_radio = page.get_by_label("Blue")
    red_radio = page.get_by_label("Red")
    yellow_radio = page.get_by_label("Yellow")
    #Step 3: Select Blue radio button
    blue_radio.check()
    #Step 4: Verify the Blue is selected
    expect(blue_radio).to_be_checked()
    #Step 5: Select Blue radio button
    red_radio.check()
    #Step 6: Verify the Red is selected
    expect(red_radio).to_be_checked()
    #Step 7: Select Yellow radio button
    yellow_radio.check()
    #Step 8: Verify the Yellow is selected
    expect(yellow_radio).to_be_checked()
    #Step 9: Verify that Blue is no longer selected
    expect(blue_radio).not_to_be_checked()
    #Step 10: Verify that Red is no longer selected
    expect(red_radio).not_to_be_checked()
    print("Radio button selection tests passed.")