<p>请求查询转帐银行响应，当执行ReqQryTransferBank后，该方法被调用。</p>
<span class="anchor" id="0fdbad5b-285b-42d4-a23c-e43b3b67d298"></span>
## 1.函数原型
<p>virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="b430e034-c027-42d6-a53f-55e60a4af569"></span>
## 2.参数
<p>pTransferBank：转帐银行</p>
<pre><code>struct CThostFtdcTransferBankField
{
    ///银行代码
    TThostFtdcBankIDType BankID;
    ///银行分中心代码
    TThostFtdcBankBrchIDType BankBrchID;
    ///银行名称
    TThostFtdcBankNameType BankName;
    ///是否活跃
    TThostFtdcBoolType IsActive;
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
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="628e5ba6-37d1-4e74-ad9a-de6e7c16a7db"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3f7526ba-56af-4a8e-8b1c-a777c3b27822"></span>
## 4.FAQ
<p>无</p>
