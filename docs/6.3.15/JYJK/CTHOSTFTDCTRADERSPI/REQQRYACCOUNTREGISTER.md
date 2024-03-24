<p>请求查询银期签约关系</p>
<p>响应: OnRspQryAccountregister</p>
<span class="anchor" id="ea6c0a29-04ad-417f-99ea-739176c35171"></span>
## 1.函数原型
<p>virtual int ReqQryAccountregister(CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID) = 0;</p>
<span class="anchor" id="5ec7828f-482c-4e95-9b0b-0eaaa4528ad6"></span>
## 2.参数
<p>pQryAccountregister：请求查询银期签约关系</p>
<pre><code>struct CThostFtdcQryAccountregisterField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///银行编码
    TThostFtdcBankIDType BankID;
    ///银行分支机构编码
    TThostFtdcBankBrchIDType BankBranchID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="fe91c361-fe6e-4a0d-92c6-e9721636f32a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="a4eab245-f45e-4449-b30b-00bbdeb395c2"></span>
## 4.调用示例
<pre><code>CThostFtdcQryAccountregisterField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.AccountID, "1000001");
strcpy_s(a.BankID, "1");
strcpy_s(a.CurrencyID, "CNY");
m_pUserApi-&gt;ReqQryAccountregister(&amp;a, 1);
</code></pre>
<span class="anchor" id="9372df02-b6df-41b1-bac9-bd1d13ad56ae"></span>
## 5.FAQ
<p>无</p>
