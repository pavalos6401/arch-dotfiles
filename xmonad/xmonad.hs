{-# LANGUAGE PartialTypeSignatures #-}
{-# OPTIONS_GHC -fno-warn-partial-type-signatures #-}

--
-- ~/.xmonad/xmonad.hs
--

-- import           System.Exit                    ( exitSuccess )

import           XMonad

import           XMonad.Config.Desktop

import           XMonad.Hooks.ManageDocks
import           XMonad.Hooks.SetWMName

import           XMonad.Layout.Spiral
import           XMonad.Layout.Tabbed
import           XMonad.Layout.ThreeColumns

import           XMonad.Util.SpawnOnce

main :: IO ()
main = do
  xmonad $ desktopConfig {
                          -- Basic
                           terminal           = myTerminal
                         , focusFollowsMouse  = myFocusFollowsMouse
                         , borderWidth        = myBorderWidth
                         , modMask            = myModKey
                         -- , workspaces         = myWorkspaces
                         , normalBorderColor  = myNormalBorderColor
                         , focusedBorderColor = myFocusedBorderColor

                         -- Bindings
                         -- , keys               = myKeys
                         -- , mouseBindings      = myMouseBindings

                         -- Hooks & Layouts
                         , layoutHook         = myLayoutHook
                         , manageHook         = myManageHook
                         , startupHook        = myStartupHook
                         }

-- Basic
myTerminal :: String
myFocusFollowsMouse :: Bool
myBorderWidth :: Dimension
myModKey :: KeyMask
-- myWorkspaces :: [String]
myNormalBorderColor :: String
myFocusedBorderColor :: String

myTerminal = "alacritty"
myFocusFollowsMouse = True
myBorderWidth = 3
myModKey = mod4Mask  -- "Windows" (super) key
-- myWorkspaces = ["1:main", "2:dev", "3:chat", "4:gam", "5:sys"]
myNormalBorderColor = "#2E3440"
myFocusedBorderColor = "#88C0D0"

-- Bindings
-- myKeys :: [(String, X ())]
-- myMouseBindings :: [(String, X ())]
--
-- myBrowser :: String
-- myBrowser = "qutebrowser"
--
-- myKeys =
--   -- XMonad
--   [ ("M-C-r"       , spawn "xmonad --recompile") -- Recompile xmonad
--   , ("M-S-r"       , spawn "xmonad --restart")   -- Restart xmonad
--   , ("M-S-q"       , io exitSuccess)             -- Quit xmonad
--
--   -- Prompt
--   , ("M-S-<Return>", spawn "rofi -show run")
--   , ("M-p"         , spawn "rofi -show drun")
--
--   -- Programs
--   , ("M-<Return>"  , spawn (myTerminal))
--   , ("M-b"         , spawn (myBrowser))
--
--   -- Kill windows
--   , ("M-S-c"       , kill1)   -- Focused
--   , ("M-S-a"       , killAll) -- All on workspace
--   ]

-- Hooks & Layouts
myLayoutHook :: _  -- Not experienced enough with Haskell to use right signature
myManageHook :: ManageHook
myStartupHook :: X ()

myLayoutHook =
  avoidStruts
    $   tiled
    ||| Mirror tiled
    ||| Full
    ||| tabbed shrinkText def
    ||| threeCol
    ||| spiral (4 / 3)
 where
  tiled    = Tall nmaster delta ratio
  threeCol = ThreeCol nmaster delta ratio
  nmaster  = 1  -- default number of windows in the master pane
  ratio    = 1 / 2  -- default proportion of screen occupied by master pane
  delta    = 2 / 100  -- percent of screen to increment by when resizing panes

myManageHook = composeAll [manageDocks]

myStartupHook = do
  spawnOnce "light-locker &"
  spawnOnce "picom &"
  spawnOnce "redshift-gtk &"
  spawnOnce "nm-applet &"
  spawnOnce "pasystray &"
  setWMName "LG3D"
