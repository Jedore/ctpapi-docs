<p>请求投资者新型组合保证金系数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPORTFMARGINRATIO/">ReqQryInvestorPortfMarginRatio</a>后，该方法被调用。</p>
<span class="anchor" id="8fbbc3eb-dc5b-44d1-885e-e5415d666d31"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorPortfMarginRatio(CThostFtdcInvestorPortfMarginRatioField *pInvestorPortfMarginRatio, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="de20af27-9294-43a3-be66-c66c545c36d4"></span>
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
<span class="anchor" id="01f18af8-553b-47c9-9df1-d111dabf8831"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="cf9e5368-1178-4dd9-9570-fc03335c2bb2"></span>
## 4.FAQ
<p>无</p>
