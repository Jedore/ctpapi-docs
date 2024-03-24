<p>报价录入请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUOTEINSERT/">ReqQuoteInsert</a>后有字段填写不对之类的CTP报错则通过此接口返回。</p>
<span class="anchor" id="488cc16b-9662-47a7-91fd-39dfece55403"></span>
## 1.函数原型
<p>virtual void OnRspQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="48f5bbc0-d878-411d-b285-d848dd75f4c2"></span>
## 2.参数
<p>pInputQuote：输入的报价</p>
<pre><code>struct CThostFtdcInputQuoteField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///报价引用
    TThostFtdcOrderRefType  QuoteRef;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///卖价格
    TThostFtdcPriceType AskPrice;
    ///买价格
    TThostFtdcPriceType BidPrice;
    ///卖数量
    TThostFtdcVolumeType    AskVolume;
    ///买数量
    TThostFtdcVolumeType    BidVolume;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///业务单元
    TThostFtdcBusinessUnitType  BusinessUnit;
    ///卖开平标志
    TThostFtdcOffsetFlagType    AskOffsetFlag;
    ///买开平标志
    TThostFtdcOffsetFlagType    BidOffsetFlag;
    ///卖投机套保标志
    TThostFtdcHedgeFlagType AskHedgeFlag;
    ///买投机套保标志
    TThostFtdcHedgeFlagType BidHedgeFlag;
    ///衍生卖报单引用
    TThostFtdcOrderRefType  AskOrderRef;
    ///衍生买报单引用
    TThostFtdcOrderRefType  BidOrderRef;
    ///应价编号
    TThostFtdcOrderSysIDType    ForQuoteSysID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///交易编码
    TThostFtdcClientIDType  ClientID;
    ///保留的无效字段
    TThostFtdcOldIPAddressType  reserve2;
    ///Mac地址
    TThostFtdcMacAddressType    MacAddress;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
        ///被顶单编号
    TThostFtdcOrderSysIDType    ReplaceSysID;
};
</code></pre>
<p>ForQuoteSysID：指定响应的是市场上哪一笔询价</p>
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
<span class="anchor" id="fe0d8382-d50c-40b9-8bc4-bbe1f943fcfd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="57fe86de-5fd0-4f31-9fc4-84b3122bfe16"></span>
## 4.FAQ
<p>无</p>
