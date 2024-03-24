<p>请求查询结算信息确认</p>
<p>响应: OnRspQrySettlementInfoConfirm</p>
<span class="anchor" id="a28c3475-a22e-45cb-9fef-48d678429ab8"></span>
## 1.函数原型
<p>virtual int ReqQrySettlementInfoConfirm(CThostFtdcQrySettlementInfoConfirmField *pQrySettlementInfoConfirm, int nRequestID) = 0;</p>
<span class="anchor" id="1603ec36-d7f1-4a31-a850-051d96219368"></span>
## 2.参数
<p>pQrySettlementInfoConfirm：查询结算信息确认域</p>
<pre><code>struct CThostFtdcQrySettlementInfoConfirmField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="121d091a-4d1e-4732-b671-afee7c17304b"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="cc8e483f-fd23-42b1-904f-3eb081b768e8"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="2bb59a0a-ea9f-4f7e-a991-f1944e20ef5f"></span>
## 5.FAQ
<p>无</p>
