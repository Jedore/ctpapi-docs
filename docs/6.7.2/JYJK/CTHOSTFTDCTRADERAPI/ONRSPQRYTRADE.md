<p>请求查询成交响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYTRADE/">ReqQryTrade</a>后，该方法被调用。</p>
<span class="anchor" id="de1720b7-75bb-468a-8a45-aaa279376d8d"></span>
## 1.函数原型
<p>virtual void OnRspQryTrade(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="df860d91-1e54-4337-ba74-6d496cd0e0c4"></span>
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
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="0f33d6a4-fa36-4375-b497-d4c2185322fd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="38bcfe59-d836-4bf9-b385-b8639a03f5f0"></span>
## 4.FAQ
<p><span alt="" id="anchor-id-10"></span> </p>
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">不同交易所，为什么TradeDate有的是自然日有的是交易日？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>TradeDate字段，大商所、郑商所回报中该字段为交易日；上期所、能源回报为自然日。</p>
<p>建议确认一笔成交的时间用Tradingday+TradeTime这一组字段。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
