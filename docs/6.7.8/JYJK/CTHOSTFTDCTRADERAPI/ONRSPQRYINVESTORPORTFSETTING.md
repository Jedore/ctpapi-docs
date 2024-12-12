<p>请求投资者投资者新组保设置查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPORTFSETTING/">ReqQryInvestorPortfSetting</a>后，该方法被调用。</p>
<span class="anchor" id="81c5e387-dacf-40ac-835f-8889259a5129"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorPortfSetting(CThostFtdcInvestorPortfSettingField *pInvestorPortfSetting, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a0753a78-fbff-48ab-8d0b-ba323ec3b0a3"></span>
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
<span class="anchor" id="d8836bbb-e57c-4cc0-9505-9c919ad5db82"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="738d16ed-4dfc-4bf8-bb73-947ae27c0b16"></span>
## 4.FAQ
<p>无</p>
