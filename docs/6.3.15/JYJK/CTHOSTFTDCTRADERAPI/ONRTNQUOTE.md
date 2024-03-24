<p>报价通知，当执行ReqQuoteInsert后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="9eaf64d0-870a-4950-9191-1883af469f32"></span>
## 1.函数原型
<p>virtual void OnRtnQuote(CThostFtdcQuoteField *pQuote) {};</p>
<span class="anchor" id="d44239f9-9136-411a-a0a3-d234fc32c19e"></span>
## 2.参数
<p>pQuote：报价</p>
<pre><code>struct CThostFtdcQuoteField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///报价引用
    TThostFtdcOrderRefType QuoteRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///卖价格
    TThostFtdcPriceType AskPrice;
    ///买价格
    TThostFtdcPriceType BidPrice;
    ///卖数量
    TThostFtdcVolumeType AskVolume;
    ///买数量
    TThostFtdcVolumeType BidVolume;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///业务单元
    TThostFtdcBusinessUnitType BusinessUnit;
    ///卖开平标志
    TThostFtdcOffsetFlagType AskOffsetFlag;
    ///买开平标志
    TThostFtdcOffsetFlagType BidOffsetFlag;
    ///卖投机套保标志
    TThostFtdcHedgeFlagType AskHedgeFlag;
    ///买投机套保标志
    TThostFtdcHedgeFlagType BidHedgeFlag;
    ///本地报价编号
    TThostFtdcOrderLocalIDType QuoteLocalID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///会员代码
    TThostFtdcParticipantIDType ParticipantID;
    ///客户代码
    TThostFtdcClientIDType ClientID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType ExchangeInstID;
    ///交易所交易员代码
    TThostFtdcTraderIDType TraderID;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///报价提示序号
    TThostFtdcSequenceNoType NotifySequence;
    ///报价提交状态
    TThostFtdcOrderSubmitStatusType OrderSubmitStatus;
    ///交易日
    TThostFtdcDateType TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType SettlementID;
    ///报价编号
    TThostFtdcOrderSysIDType QuoteSysID;
    ///报单日期
    TThostFtdcDateType InsertDate;
    ///插入时间
    TThostFtdcTimeType InsertTime;
    ///撤销时间
    TThostFtdcTimeType CancelTime;
    ///报价状态
    TThostFtdcOrderStatusType QuoteStatus;
    ///结算会员编号
    TThostFtdcParticipantIDType ClearingPartID;
    ///序号
    TThostFtdcSequenceNoType SequenceNo;
    ///卖方报单编号
    TThostFtdcOrderSysIDType AskOrderSysID;
    ///买方报单编号
    TThostFtdcOrderSysIDType BidOrderSysID;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///用户端产品信息
    TThostFtdcProductInfoType UserProductInfo;
    ///状态信息
    TThostFtdcErrorMsgType StatusMsg;
    ///操作用户代码
    TThostFtdcUserIDType ActiveUserID;
    ///经纪公司报价编号
    TThostFtdcSequenceNoType BrokerQuoteSeq;
    ///衍生卖报单引用
    TThostFtdcOrderRefType AskOrderRef;
    ///衍生买报单引用
    TThostFtdcOrderRefType BidOrderRef;
    ///应价编号
    TThostFtdcOrderSysIDType ForQuoteSysID;
    ///营业部编号
    TThostFtdcBranchIDType BranchID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///资金账号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>QuoteStatus：报价的状态</p>
<p>StatusMsg：明文显示状态信息</p>
<span class="anchor" id="93fa429d-728b-4e0d-aa48-3a5d3b8637d5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="7a87c908-4f54-476d-8afb-9a4d06164f66"></span>
## 4.FAQ
<p>无</p>
