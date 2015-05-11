#!/bin/env python

def var( tree, varName, type=float ):
    tree.var(varName, type)

def fill( tree, varName, value ):
    tree.fill( varName, value )

# simple particle

def bookParticle( tree, pName ):
    var(tree, '{pName}_e'.format(pName=pName))
    var(tree, '{pName}_theta'.format(pName=pName))
    var(tree, '{pName}_phi'.format(pName=pName))
    var(tree, '{pName}_m'.format(pName=pName))

def fillParticle( tree, pName, particle ):
    fill(tree, '{pName}_e'.format(pName=pName), particle.e() )
    fill(tree, '{pName}_theta'.format(pName=pName), particle.theta() )
    fill(tree, '{pName}_phi'.format(pName=pName), particle.phi() )
    fill(tree, '{pName}_m'.format(pName=pName), particle.m() )
    
# jet

def bookJet( tree, pName ):
    bookParticle(tree, pName )
    # var(tree, '{pName}_npart'.format(pName=pName))

def fillJet( tree, pName, jet ):
    fillParticle(tree, pName, jet )
    # fill(tree, '{pName}_npart'.format(pName=pName), len(jet.particles) )

