# Chimera Failure Map

Use this when deciding where the failure really lives.

## Structural Failures

- wrong report path
- stale wrapper or front door
- required field missing
- phase packet missing
- Task Flow or Lobster points at the wrong workflow

## Behavioral Failures

- no-trade should have won but did not
- wrong phase promotion
- entry-watch should have held but activation won
- active trade exists but management logic is weak
- closeout exists but does not judge the earlier path honestly

## Reasoning Failures

- wrong symbol won for weak reasons
- right symbol won for the wrong reasons
- alternative case not compared honestly
- packet passes structure checks but is not decision-useful
- consumer reasoning depends on helper-grade evidence without saying so

## Simulation Failures

- replay is too clean to expose real producer/consumer problems
- expected outcome is derived from the same artifact under test
- mutation cases are missing
- scenario pack covers only happy paths

## Ownership Failures

- scripts prove artifacts but no one proves decision causality
- consumer exists but does not act
- learning capture exists but does not create real next fixes
