<p>报价录入错误回报，当执行ReqQuoteInsert后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="7cedad68-0fd4-4233-8490-72be77528173"></span>
## 1.函数原型
<p>virtual void OnErrRtnQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="8ba634b3-70a1-4d56-a1ab-9b16ba1d17e4"></span>
## 2.参数
<p>pInputQuote：输入的报价</p>
<pre><code>struct CThostFtdcInputQuoteField
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
    ///衍生卖报单引用
    TThostFtdcOrderRefType AskOrderRef;
    ///衍生买报单引用
    TThostFtdcOrderRefType BidOrderRef;
    ///应价编号
    TThostFtdcOrderSysIDType ForQuoteSysID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///交易编码
    TThostFtdcClientIDType ClientID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>ForQuoteSysID：应价编号对应市场上询价的编号</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="d3d091e6-8d5b-439b-9b89-f1036895fbc6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="9a7bac3e-c64c-4978-a343-9e23b91b3460"></span>
## 4.FAQ
<p>无</p>
