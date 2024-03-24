<p>请求查询结算信息确认</p>
<p>响应: OnRspQrySettlementInfoConfirm</p>
<span class="anchor" id="f7410f49-3a35-4ffc-87b8-98c45d092c8c"></span>
## 1.函数原型
<p>virtual int ReqQrySettlementInfoConfirm(CThostFtdcQrySettlementInfoConfirmField *pQrySettlementInfoConfirm, int nRequestID) = 0;</p>
<span class="anchor" id="4b021209-b505-4a75-a8a8-b2326d18136b"></span>
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
<span class="anchor" id="06bdf12a-783f-4994-9f1c-ec8dedc09502"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2c1d0a25-c3e4-4db0-851d-ea8a7b81bcb7"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="a2844a4c-efc2-479c-9658-8b2861cc8289"></span>
## 5.FAQ
<p>无</p>
