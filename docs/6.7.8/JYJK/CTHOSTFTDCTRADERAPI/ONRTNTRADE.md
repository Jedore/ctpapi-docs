<p>成交通知，报单发出后有成交则通过此接口返回。私有流</p>
<span class="anchor" id="8f6279ba-b6df-4844-8255-d1c28e3392c7"></span>
## 1.函数原型
<p>virtual void OnRtnTrade(CThostFtdcTradeField *pTrade) {};</p>
<span class="anchor" id="9efcc8cd-bbeb-4d29-990b-ba08c6ea1ec6"></span>
## 2.参数
<p>pTrade：成交</p>
<pre><code>struct CThostFtdcTradeField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///报单引用
    TThostFtdcOrderRefType  OrderRef;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///成交编号
    TThostFtdcTradeIDType   TradeID;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///报单编号
    TThostFtdcOrderSysIDType    OrderSysID;
    ///会员代码
    TThostFtdcParticipantIDType ParticipantID;
    ///客户代码
    TThostFtdcClientIDType  ClientID;
    ///交易角色
    TThostFtdcTradingRoleType   TradingRole;
    ///保留的无效字段
    TThostFtdcOldExchangeInstIDType reserve2;
    ///开平标志
    TThostFtdcOffsetFlagType    OffsetFlag;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///价格
    TThostFtdcPriceType Price;
    ///数量
    TThostFtdcVolumeType    Volume;
    ///成交时期
    TThostFtdcDateType  TradeDate;
    ///成交时间
    TThostFtdcTimeType  TradeTime;
    ///成交类型
    TThostFtdcTradeTypeType TradeType;
    ///成交价来源
    TThostFtdcPriceSourceType   PriceSource;
    ///交易所交易员代码
    TThostFtdcTraderIDType  TraderID;
    ///本地报单编号
    TThostFtdcOrderLocalIDType  OrderLocalID;
    ///结算会员编号
    TThostFtdcParticipantIDType ClearingPartID;
    ///业务单元
    TThostFtdcBusinessUnitType  BusinessUnit;
    ///序号
    TThostFtdcSequenceNoType    SequenceNo;
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType  SettlementID;
    ///经纪公司报单编号
    TThostFtdcSequenceNoType    BrokerOrderSeq;
    ///成交来源
    TThostFtdcTradeSourceType   TradeSource;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType    ExchangeInstID;
};
</code></pre>
<p>TradeType：成交类型，<a href="../../../qtywgz/bjhxj.html#anchor-id-02">报价中的情况</a></p>
<span class="anchor" id="e2ea8938-f296-4bac-846c-1c0c54653979"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d26b70db-904a-4e51-a045-433f828df2c7"></span>
## 4.FAQ
<p><span alt="" id="anchor-id-10"></span> </p>
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">不同交易所，为什么TradeDate有的是自然日有的是交易日？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>TradeDate字段，大商所、郑商所回报中该字段为交易日；上期所、能源回报为自然日。</p>
<p>建议确认一笔成交的时间用Tradingday+TradeTime这一组字段。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><span alt="" id="anchor-id-11"></span> </p>
<p><div class="region_i"><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">成交中的，PriceSource（成交价来源）是什么意思？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>报单撮合产生的最新成交价取买价、卖价及前成交价三者居中的价格。</p>
<p>买价≥卖价≥前成交价, 最新成交价=卖价</p>
<p>买价≥前成交价≥卖价, 最新成交价=前成交价</p>
<p>前成交价≥买价≥卖价, 最新成交价=买价</p>
<p>和头文件的三个枚举值匹配</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
