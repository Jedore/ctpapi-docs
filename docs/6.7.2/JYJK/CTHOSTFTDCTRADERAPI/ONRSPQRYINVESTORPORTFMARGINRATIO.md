<p>请求投资者新型组合保证金系数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPORTFMARGINRATIO/">ReqQryInvestorPortfMarginRatio</a>后，该方法被调用。</p>
<span class="anchor" id="a759f378-c8b7-4767-b66f-eaa3e152a47b"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorPortfMarginRatio(CThostFtdcInvestorPortfMarginRatioField *pInvestorPortfMarginRatio, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8d0f2ba8-c167-4f76-97c7-d9eed174fc9d"></span>
## 2.参数
<p>pInvestorPortfMarginRatio：投资者新型组合保证金系数</p>
<pre><code>struct CThostFtdcInvestorPortfMarginRatioField
{
    ///投资者范围
    TThostFtdcInvestorRangeType InvestorRange;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///会员对投资者收取的保证金和交易所对投资者收取的保证金的比例
    TThostFtdcRatioType MarginRatio;
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
<span class="anchor" id="850cf619-cb43-453a-a943-bd8019aec4d4"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e7f656b3-5604-4783-b7a6-0fb5f3a3ce8e"></span>
## 4.FAQ
<p>无</p>
