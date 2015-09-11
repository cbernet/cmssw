#!/bin/env python

def var( tree, varName, type=float ):
    tree.var(varName, type)

def fill( tree, varName, value ):
    tree.fill( varName, value )

# simple particle

def bookParticle( tree, pName ):
    var(tree, '{pName}_pdgid'.format(pName=pName))
    var(tree, '{pName}_e'.format(pName=pName))
    var(tree, '{pName}_pt'.format(pName=pName))
    var(tree, '{pName}_theta'.format(pName=pName))
    var(tree, '{pName}_eta'.format(pName=pName))
    var(tree, '{pName}_phi'.format(pName=pName))
    var(tree, '{pName}_m'.format(pName=pName))

def fillParticle( tree, pName, particle ):
    fill(tree, '{pName}_pdgid'.format(pName=pName), particle.pdgid() )
    fill(tree, '{pName}_e'.format(pName=pName), particle.e() )
    fill(tree, '{pName}_pt'.format(pName=pName), particle.pt() )
    fill(tree, '{pName}_theta'.format(pName=pName), particle.theta() )
    fill(tree, '{pName}_eta'.format(pName=pName), particle.eta() )
    fill(tree, '{pName}_phi'.format(pName=pName), particle.phi() )
    fill(tree, '{pName}_m'.format(pName=pName), particle.m() )

def bookMet(tree, pName):
    var(tree, '{pName}_pt'.format(pName=pName))
    var(tree, '{pName}_phi'.format(pName=pName))
    var(tree, '{pName}_sumet'.format(pName=pName))

def fillMet(tree, pName, met):
    fill(tree, '{pName}_pt'.format(pName=pName), met.pt())
    fill(tree, '{pName}_phi'.format(pName=pName), met.phi())
    fill(tree, '{pName}_sumet'.format(pName=pName), met.sumEt())
