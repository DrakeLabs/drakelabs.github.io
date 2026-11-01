# DrakeLabs public service status

Public page: https://status.drakelabs.org/

Zach created the Better Stack account, monitors, and public status page. The page was inspected in the browser and displayed both service endpoints as operational at the time of inspection. These observations are not hard-coded into the portfolio.

## Website integration

The footer's Service status link opens the public page directly. The retained /status/ route explains the checks and offers the same link. All sample incidents, sample states, and fake check timestamps were removed. The static website does not poll services, store credentials, copy uptime percentages, or embed a potentially stale status result.

Better Stack monitors the public Jellyfin and Requests addresses. HTTP availability does not certify playback or request fulfillment, and it does not identify whether an outage originates in an app, Cloudflare, or the home connection. Monitor configuration and alert delivery have not been independently audited or tested by interrupting services.

## Remaining setup

- Public display names are Jellyfin and Media Requests, verified November 1, 2026.
- Zach confirmed receipt of a test alert. No live service outage was induced.
- Review incident and maintenance update settings before publishing announcements or enabling subscriber notifications.
- Zach configured status.drakelabs.org through Better Stack and Cloudflare. The custom HTTPS address was verified in the browser November 1, 2026 and showed both services operational. The assistant made no DNS changes.
- Link the status-page logo back to the portfolio once its public website address is working.

Keep detailed internal metrics, tunnel identifiers, credentials, and private diagnostics out of the public page and static build. The hosted provider owns current availability results and history.
