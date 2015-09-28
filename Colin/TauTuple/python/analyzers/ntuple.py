#!/bin/env python

def var( tree, varName, type=float ):
    tree.var(varName, type)

def fill( tree, varName, value ):
    tree.fill( varName, value )

# event information

def bookEvent(tree): 
    var(tree, 'run')
    var(tree, 'lumi')
    var(tree, 'event')
 
def fillEvent(tree, event):
    fill(tree, 'run', event.run)
    fill(tree, 'lumi', event.lumi)
    fill(tree, 'event', event.eventId)


# simple particle

def bookParticle( tree, pName ):
    var(tree, '{pName}_pdgid'.format(pName=pName))
    var(tree, '{pName}_e'.format(pName=pName))
    var(tree, '{pName}_pt'.format(pName=pName))
    var(tree, '{pName}_eta'.format(pName=pName))
    var(tree, '{pName}_phi'.format(pName=pName))
    var(tree, '{pName}_m'.format(pName=pName))

def fillParticle( tree, pName, particle ):
    fill(tree, '{pName}_pdgid'.format(pName=pName), particle.pdgId() )
    fill(tree, '{pName}_e'.format(pName=pName), particle.energy() )
    fill(tree, '{pName}_pt'.format(pName=pName), particle.pt() )
    fill(tree, '{pName}_eta'.format(pName=pName), particle.eta() )
    fill(tree, '{pName}_phi'.format(pName=pName), particle.phi() )
    fill(tree, '{pName}_m'.format(pName=pName), particle.mass() )

def bookMet(tree, pName):
    var(tree, '{pName}_pt'.format(pName=pName))
    var(tree, '{pName}_phi'.format(pName=pName))
    var(tree, '{pName}_sumet'.format(pName=pName))

def fillMet(tree, pName, met):
    fill(tree, '{pName}_pt'.format(pName=pName), met.pt())
    fill(tree, '{pName}_phi'.format(pName=pName), met.phi())
    fill(tree, '{pName}_sumet'.format(pName=pName), met.sumEt())

def bookTau(tree, pName, tau):
    bookParticle(tree, pName)
    for discName in tau.discs:
        var(tree, '{pName}_{disc}'.format(pName=pName,
                                          disc=discName))
        
def fillTau(tree, pName, tau):
    fillParticle(tree, pName, tau)
    for discName, value in tau.discs.iteritems():
        fill(tree, '{pName}_{disc}'.format(pName=pName,
                                           disc=discName), value)

