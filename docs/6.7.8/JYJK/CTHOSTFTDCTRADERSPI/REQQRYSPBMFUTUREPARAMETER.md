<p>请求SPBM期货合约参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMFUTUREPARAMETER/">OnRspQrySPBMFutureParameter</a></p>
<span class="anchor" id="8c91aee3-9af7-46dc-a11d-22cccbd3716f"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMFutureParameter(CThostFtdcQrySPBMFutureParameterField *pQrySPBMFutureParameter, int nRequestID) = 0;</p>
<span class="anchor" id="405e2b30-a236-4413-a649-d2b8276ef18b"></span>
## 2.参数
<p>pQrySPBMFutureParameter：SPBM期货合约保证金参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">品种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="0c5ff2c2-7a14-49a8-a18c-0e2c5097c681"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2cf74f53-5750-4c8e-91a0-872f02f020c2"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="87fb7b9f-6b05-479b-8ea9-309b6f76f2a1"></span>
## 5.FAQ
<p>无</p>