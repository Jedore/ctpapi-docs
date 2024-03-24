<p>请求查询银期签约关系</p>
<p>响应: OnRspQryAccountregister</p>
<span class="anchor" id="639aedb3-a670-421d-976b-113e43cdea26"></span>
## 1.函数原型
<p>virtual int ReqQryAccountregister(CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID) = 0;</p>
<span class="anchor" id="fc55e26e-9b5a-4e17-8cdb-0646d849bd8a"></span>
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
<span class="anchor" id="abf7c406-47bb-423e-bbe5-161ab9e20319"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="15c8d4e2-bcc5-4c82-ae6b-391a20023083"></span>
## 4.调用示例
<pre><code>CThostFtdcQryAccountregisterField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.AccountID, "1000001");
strcpy_s(a.BankID, "1");
strcpy_s(a.CurrencyID, "CNY");
m_pUserApi-&gt;ReqQryAccountregister(&amp;a, 1);
</code></pre>
<span class="anchor" id="69f1c9bf-10f7-43ed-839c-09062d2e12d1"></span>
## 5.FAQ
<p>无</p>
