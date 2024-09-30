<p>请求投资者投资者新组保设置查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPORTFSETTING/">ReqQryInvestorPortfSetting</a>后，该方法被调用。</p>
<span class="anchor" id="d75c6ecf-4ea7-41fb-95da-27fc2d1366b2"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorPortfSetting(CThostFtdcInvestorPortfSettingField *pInvestorPortfSetting, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="dec66677-fdba-4b27-bad4-e97b993655d6"></span>
## 2.参数
<p>pInvestorPortfSetting：投资者新组保设置</p>
<pre><code>struct CThostFtdcInvestorPortfSettingField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者编号
    TThostFtdcInvestorIDType    InvestorID;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///是否开启新组保
    TThostFtdcBoolType  UsePortf;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType   ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType  ErrorMsg;
};
</code></pre>
<span class="anchor" id="8673738d-a2e9-4aac-9215-e7daaf0554c3"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5c301b9f-83a1-45a4-9581-50cf4f3a2159"></span>
## 4.FAQ
<p>无</p>
