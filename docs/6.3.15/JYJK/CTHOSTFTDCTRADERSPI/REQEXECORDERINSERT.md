<p>执行宣告录入请求</p>
<p>错误响应: OnErrRtnExecOrderInsert，OnRspExecOrderInsert</p>
<p>正确响应: OnRtnExecOrder</p>
<span class="anchor" id="38107a7f-3b1e-49bc-9c83-e1686b130691"></span>
## 1.函数原型
<p>virtual int ReqExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, int nRequestID) = 0;</p>
<span class="anchor" id="8408039b-ba83-4755-9e38-35ccd122631a"></span>
## 2.参数
<p>pInputExecOrder：输入的执行宣告</p>
<pre><code>struct CThostFtdcInputExecOrderField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///执行宣告引用
    TThostFtdcOrderRefType ExecOrderRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///数量
    TThostFtdcVolumeType Volume;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///业务单元
    TThostFtdcBusinessUnitType BusinessUnit;
    ///开平标志
    TThostFtdcOffsetFlagType OffsetFlag;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///执行类型
    TThostFtdcActionTypeType ActionType;
    ///保留头寸申请的持仓方向
    TThostFtdcPosiDirectionType PosiDirection;
    ///期权行权后是否保留期货头寸的标记,该字段已废弃
    TThostFtdcExecOrderPositionFlagType ReservePositionFlag;
    ///期权行权后生成的头寸是否自动平仓
    TThostFtdcExecOrderCloseFlagType CloseFlag;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///资金账号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///交易编码
    TThostFtdcClientIDType ClientID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="eb37ca8c-b7ca-4151-a18b-6a62770cf180"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ae4a81b5-b721-452e-9f9c-7ba40d8048bb"></span>
## 4.调用示例
<pre><code>CThostFtdcInputExecOrderField OrderInsert = { 0 };
strcpy_s(OrderInsert.BrokerID, "9999");
strcpy_s(OrderInsert.InvestorID, "1000001");
strcpy_s(OrderInsert.InstrumentID, "rb1809");
strcpy_s(OrderInsert.ExchangeID, "SHFE");
strcpy_s(OrderInsert.ExecOrderRef, "00001");
strcpy_s(OrderInsert.UserID, "1000001");
OrderInsert.Volume = 1;
OrderInsert.RequestID = 1; 
OrderInsert.OffsetFlag = THOST_FTDC_OF_Close;//开平标志
OrderInsert.HedgeFlag = THOST_FTDC_HF_Speculation;//投机套保标志
OrderInsert.ActionType = THOST_FTDC_ACTP_Exec;//执行类型类型
OrderInsert.PosiDirection = THOST_FTDC_PD_Long;//持仓多空方向类型
OrderInsert.ReservePositionFlag = THOST_FTDC_EOPF_Reserve;//期权行权后是否保留期货头寸的标记类型
OrderInsert.CloseFlag = THOST_FTDC_EOCF_NotToClose;//期权行权后生成的头寸是否自动平仓类型
m_pUserApi-&gt;ReqExecOrderInsert(&amp;OrderInsert, nRequestID++);
</code></pre>
<span class="anchor" id="e29be22c-3067-4167-b692-b4e5040644bd"></span>
## 5.FAQ
<p>无</p>
