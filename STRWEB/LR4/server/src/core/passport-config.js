import passport from "passport";
import { Strategy as LocalStrategy } from "passport-local";
import { Strategy as GoogleStrategy } from "passport-google-oauth20";
import { Strategy as FacebookStrategy } from "passport-facebook";
import { AuthService } from "../services/auth/auth.js";
import { CONFIG } from "./config.js";

const authService = new AuthService();

passport.use(
  new LocalStrategy(
    { usernameField: "email", passwordField: "password" },
    async (email, password, done) => {
      try {
        const tokens = await authService.signInUser({ email, password });
        return typeof tokens === "string"
          ? done(null, false, { message: tokens })
          : done(null, tokens);
      } catch (e) {
        console.error(e);
        return done(e);
      }
    }
  )
);

passport.use(
  new GoogleStrategy(
    {
      clientID: CONFIG.GOOGLE_CLIENT_ID,
      clientSecret: CONFIG.GOOGLE_CLIENT_SECRET,
      callbackURL: CONFIG.GOOGLE_CALLBACK,
      scope: ["profile", "email"],
    },
    async (_, __, profile, done) => {
      try {
        const { email, name, email_verified } = profile._json;
        if (!email || !email_verified || !name)
          return done(null, false, {
            message:
              "You can't login with Google Account, because it doesn't provide minimal nessesary info (verified email & name)!",
          });
        const tokens = await authService.authWithAccount({ email, name });
        return typeof tokens === "string"
          ? done(null, false, { message: tokens })
          : done(null, tokens);
      } catch (e) {
        console.log(e);
        return done(e);
      }
    }
  )
);

passport.use(
  new FacebookStrategy(
    {
      clientID: CONFIG.FACEBOOK_CLIENT_ID,
      clientSecret: CONFIG.FACEBOOK_CLIENT_SECRET,
      callbackURL: CONFIG.FACEBOOK_CALLBACK,
      scope: ["email", "public_profile"],
      profileFields: ["id", "displayName", "email"],
    },
    async (_, __, profile, done) => {
      try {
        const { name, email } = profile._json;
        if (!email || !name)
          return done(null, false, {
            message:
              "You can't login with Facebook Account, because it doesn't provide minimal nessesary info (email & name)!",
          });
        const tokens = await authService.authWithAccount({ email, name });
        return typeof tokens === "string"
          ? done(null, false, { message: tokens })
          : done(null, tokens);
      } catch (e) {
        console.error(e);
        return done(e);
      }
    }
  )
);

export default passport;
